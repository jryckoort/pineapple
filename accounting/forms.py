from django import forms
from .models import AccountingEntry

class AccountingEntryForm(forms.ModelForm):
    class Meta:
        model = AccountingEntry
        fields = '__all__'

    def clean(self):
        cleaned_data = super(AccountingEntryForm, self).clean()
        counterparty_account = cleaned_data.get('counterparty_account')
        compensation_account = cleaned_data.get('compensation_account')

        if counterparty_account and compensation_account:
            self.add_error("counterparty_account",
                "Vous ne pouvez pas remplir les champs Contrepartie et Compensation en même temps !"
                )

        return cleaned_data
