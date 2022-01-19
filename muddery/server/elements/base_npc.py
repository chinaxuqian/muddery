"""
None Player Characters

Player Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""

import traceback
from muddery.server.utils.logger import logger
from muddery.server.utils.dialogue_handler import DialogueHandler
from muddery.server.mappings.element_set import ELEMENT
from muddery.server.database.worlddata.npc_dialogues import NPCDialogues
from muddery.server.database.worlddata.npc_shops import NPCShops
from muddery.server.database.worlddata.worlddata import WorldData
from muddery.server.utils import defines
from muddery.server.utils.localized_strings_handler import _


class MudderyBaseNPC(ELEMENT("CHARACTER")):
    """
    The character not controlled by players.

    States:
        shops
    """
    element_type = "BASE_NPC"
    element_name = "Base None Player Character"
    model_name = ""

    async def at_element_setup(self, first_time):
        """
        Init the character.
        """
        await super(MudderyBaseNPC, self).at_element_setup(first_time)

        # Character can auto fight.
        self.auto_fight = True

        # load dialogues.
        self.load_dialogues()

        # load shops
        await self.load_shops()

    def load_dialogues(self):
        """
        Load dialogues.
        """
        dialogues = NPCDialogues.get(self.get_element_key())

        self.default_dialogues = [dialogue.dialogue for dialogue in dialogues if dialogue.dialogue and dialogue.default]
        self.dialogues = [dialogue.dialogue for dialogue in dialogues if dialogue.dialogue and not dialogue.default]

    async def load_shops(self):
        """
        Load character's shop.
        """
        # shops records
        shop_records = NPCShops.get(self.get_element_key())
        shop_keys = set([record.shop for record in shop_records])
        base_model = ELEMENT("SHOP").get_base_model()

        # NPC's shop
        self.shops = {}
        for key in shop_keys:
            try:
                table_data = WorldData.get_table_data(base_model, key=key)
                table_data = table_data[0]

                shop = ELEMENT(table_data.element_type)()
                await shop.setup_element(key)
                shop.set_owner(self)
                self.shops[key] = shop
            except Exception as e:
                logger.log_err("Can not create shop %s: (%s)%s" % (key, type(e).__name__, e))
                continue

    async def get_shop_info(self, shop_key, caller):
        """
        Show shop's information to the player.
        :param shop_key:
        :param caller:
        :return:
        """
        if shop_key not in self.shops:
            return None

        shop_info = await self.shops[shop_key].get_info(caller)
        shop_info["npc"] = self.get_id()
        return shop_info

    async def sell_goods(self, shop_key, goods_index, caller):
        """
        Sell goods to the caller.
        :param shop_key:
        :param goods_index:
        :param caller:
        :return:
        """
        if shop_key not in self.shops:
            return None

        await self.shops[shop_key].sell_goods(goods_index, caller)

    async def get_available_commands(self, caller):
        """
        This returns a list of available commands.
        """
        commands = []
        if await self.is_alive():
            if self.dialogues or self.default_dialogues:
                # If the character have something to talk, add talk command.
                commands.append({"name": _("Talk"), "cmd": "talk", "args": self.get_id()})

            # Add shops.
            for key, obj in self.shops.items():
                if not await obj.is_available(caller):
                    continue

                verb = obj.get_verb()
                commands.append({
                    "name": verb,
                    "cmd": "shopping",
                    "args": {
                        "npc": self.get_id(),
                        "shop": obj.get_element_key(),
                    }
                })

            if self.friendly <= 0:
                commands.append({"name": _("Attack"), "cmd": "attack", "args": self.get_id()})

        return commands

    async def have_quest(self, caller):
        """
        If the npc can complete or provide quests.
        Returns (can_provide_quest, can_complete_quest).
        """
        return await DialogueHandler.inst().have_quest(caller, self)

    async def remove_from_combat(self):
        """
        Removed from the current combat.
        """
        status = None
        opponents = None
        rewards = None

        combat = await self.get_combat()
        if combat:
            result = combat.get_combat_result(self.id)
            if result:
                status, opponents, rewards = result

        if not self.is_temp:
            if status == defines.COMBAT_LOSE:
                await self.die(opponents)

        await super(MudderyBaseNPC, self).remove_from_combat()

        if not self.is_temp:
            if status != defines.COMBAT_LOSE:
                await self.recover()
