from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

from .models import Team, Stadium, City
from .forms import TeamForm, UpdateTeamForm, StadiumForm, UpdateStadiumForm, CityForm, UpdateCityForm,PlayerForm,UpdatePlayerForm,player

# Create your views here.

### T E A M ###

# list
class ListTeam(generic.View):
    template_name = "core/team/list_team.html"
    context = {}

    def get(self, request, *args, **kwargs):
        #lleva s
        teams = Team.objects.filter(status=True)
        self.context = {
            "teams": teams
        }
        return render(request, self.template_name, self.context)

# detail
class DetailTeam(generic.View):
    template_name = "core/team/detail_team.html"
    context = {}

    def get(self, request, pk, *args, **kargs):
        #no lleva s
        team = Team.objects.get(pk=pk)
        self.context = {
            "team": team
        }
        return render(request, self.template_name, self.context)

# create
class CreateTeam(generic.CreateView):
    template_name = "core/team/create_team.html"
    context = {}
    form_class = TeamForm
    success_url = reverse_lazy("core:list_team")

# update
class UpdateTeam(generic.UpdateView):
    template_name = "core/team/update_team.html"
    model = Team
    form_class = UpdateTeamForm
    success_url = reverse_lazy("core:list_team")

# delete
class DeleteTeam(generic.DeleteView):
    template_name = "core/team/delete_team.html"
    model = Team
    success_url = reverse_lazy("core:list_team")

#-------------------------------------------------------------------------#

### S T A D I U M ###
class ListStadium(generic.View):
    template_name = "core/stadium/list_stadium.html"
    context = {}

    def get(self, request, *args, **kwargs):
        stadiums = Stadium.objects.filter(status=True)
        self.context = {
            "stadiums": stadiums
        }
        return render(request, self.template_name, self.context)

# detail
class DetailStadium(generic.View):
    template_name = "core/stadium/detail_stadium.html"
    context = {}

    def get(self, request, pk, *args, **kargs):
        #no lleva s
        stadium = Stadium.objects.get(pk=pk)
        self.context = {
            "stadium": stadium
        }
        return render(request, self.template_name, self.context)

# create
class CreateStadium(generic.CreateView):
    template_name = "core/stadium/create_stadium.html"
    context = {}
    form_class = StadiumForm
    success_url = reverse_lazy("core:list_stadium")

# update
class UpdateStadium(generic.UpdateView):
    template_name = "core/stadium/update_stadium.html"
    model = Stadium
    form_class = UpdateStadiumForm
    success_url = reverse_lazy("core:list_stadium")

# delete
class DeleteStadium(generic.DeleteView):
    template_name = "core/stadium/delete_stadium.html"
    model = Stadium
    success_url = reverse_lazy("core:list_stadium")

#-------------------------------------------------------------------------#

### C I T Y ###

# list
class ListCity(generic.View):
    template_name = "core/city/list_city.html"
    context = {}

    def get(self, request, *args, **kwargs):
        #lleva s
        citys = City.objects.filter(status=True)
        self.context = {
            "citys": citys
        }
        return render(request, self.template_name, self.context)

class DetailCity(generic.View):
    template_name = "core/city/detail_city.html"
    context = {}

    def get(self, request, pk, *args, **kargs):
        city = City.objects.get(pk=pk)
        self.context = {
            "city": city
        }
        return render(request, self.template_name, self.context)

# create
class CreateCity(generic.CreateView):
    template_name = "core/city/create_city.html"
    context = {}
    form_class = CityForm
    success_url = reverse_lazy("core:list_city")

# update
class UpdateCity(generic.UpdateView):
    template_name = "core/city/update_city.html"
    model = City
    form_class = UpdateCityForm
    success_url = reverse_lazy("core:list_city")

# delete
class DeleteCity(generic.DeleteView):
    template_name = "core/city/delete_city.html"
    model = City
    success_url = reverse_lazy("core:list_city")

    #-------------------------------------------------------------------------#

### P L A Y E R S ###

# list
class ListPlayer(generic.View):
    template_name = "core/players/list_players.html"
    context = {}

    def get(self, request, *args, **kwargs):
        #lleva s
        players = Team.player.filter(status=True)
        self.context = {
            "players": players
        }
        return render(request, self.template_name, self.context)

# create
class CreatePlayer(generic.CreateView):
    template_name = "core/players/create_players.html"
    context = {}
    form_class = PlayerForm
    success_url = reverse_lazy("core:list_players")

# update
class UpdatePlayer(generic.UpdateView):
    template_name = "core/team/update_players.html"
    model = player
    form_class = UpdatePlayerForm
    success_url = reverse_lazy("core:list_players")

# delete
class DeleteTeam(generic.DeleteView):
    template_name = "core/team/delete_players.html"
    model = Player
    success_url = reverse_lazy("core:list_players")


