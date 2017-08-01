from django.contrib import admin

from .models import  CustomUser, Agent, Candidate


class AgentAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display = ('id', 'user')
    search_fields = ('user',)
    list_per_page = 10
    
    
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user',)
    list_per_page = 10


admin.site.register(CustomUser)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Candidate, CandidateAdmin)