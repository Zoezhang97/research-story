from django import forms

from meeting.models import Link


class MeetingForm(forms.ModelForm):
    """create a meeting sechdule"""

    class Meta:
        model = Link
        fields = ('meeting_name',
                  'meeting_link',
                  'start_time',
                  'end_time',

                  'monday',
                  'tuesday',
                  'wednesday',
                  'thursday',
                  'friday',
                  'saturday',
                  'sunday',
                  )
