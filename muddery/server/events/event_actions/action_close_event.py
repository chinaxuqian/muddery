"""
Event action.
"""

from muddery.server.events.base_event_action import BaseEventAction
from muddery.server.database.worlddata.worlddata import WorldData


class ActionCloseEvent(BaseEventAction):
    """
    Close events.
    """
    key = "ACTION_CLOSE_EVENT"
    name = "Close an Event"
    model_name = "action_close_event"
    repeatedly = False

    async def func(self, event_key, character, obj):
        """
        Close an event.

        Args:
            event_key: (string) event's key.
            character: (object) relative character.
            obj: (object) the event object.
        """
        # get action data
        records = WorldData.get_table_data(self.model_name, event_key=event_key)

        for record in records:
            # Close event.
            await character.close_event(record.event)
