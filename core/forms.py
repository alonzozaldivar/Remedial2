from django import forms

from .models import Team, Stadium, City, Player

# T E A M
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "venue",
            "team_name",
            "players",
            "director",
        ]
        widgets = {
            "venue": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "players": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "director": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
        }

class UpdateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "venue",
            "team_name",
            "players",
            "director",
        ]
        widgets = {
            "venue": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "players": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "director": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
        }

#-----------------------------------------------------------------------------------------------------------------#

# S T A D I U M
class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = [
            "city",
            "stadium_name",
            "team",
            "capacity",
        ]
        widgets = {
            "city": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "stadium_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "capacity": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
        }

class UpdateStadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = [
            "city",
            "stadium_name",
            "team",
            "capacity",
        ]
        widgets = {
            "city": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "stadium_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "capacity": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
        }

# ------------------------------------------------------------------------------------------------------------------#

# C I T Y
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            "city_name",
        ]
        widgets = {
            "city_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
        }

class UpdateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            "city_name",
        ]
        widgets = {
            "city_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
        }

# -----------------------------------------

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "team",
            "player_name",
            "number",
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "player_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "number": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
        }

class UpdatePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "team",
            "player_name",
            "number",
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "player_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "number": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
        }