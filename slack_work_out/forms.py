from django import forms

from .models import WorkOut


class CreateLogForm(forms.ModelForm):
    """管理者がarticleを作成するフォーム"""

    class Meta:
        model = WorkOut
        fields = ('user',)
        labels = {
            'user': 'name'
        }

    def save(self, commit=False):
        log = super().save(commit=False)
        log.save()
        return log
