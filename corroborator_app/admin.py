from django.contrib import admin
from corroborator_app.models import (
    Incident,
    CrimeCategory,
    Actor,
    Bulletin,
    TimeInfo,
    Location,
    Source,
   StatusUpdate,
    ActorRole,
    Label,
    SourceType,
    Comment,
    Media,
    PredefinedSearch,
    ActorRelationship,
    ActorCondition,
    ActorStatus,
    EventType,
    RoleType,
    RelationType
)

import reversion


class CommentsInlineIn(admin.TabularInline):
    model = Incident.incident_comments.through
    extra = 1


class LocationInlineIn(admin.TabularInline):
    model = Incident.locations.through
    extra = 1


class TimeInfoInlineIn(admin.StackedInline):
    model = Incident.times.through
    extra = 1


class ActorsRoleInlineIn(admin.TabularInline):
    model = Incident.actors_role.through
    extra = 1


class LabelInlineIn(admin.TabularInline):
    model = Incident.labels.through
    extra = 1


class CrimesInlineIn(admin.TabularInline):
    model = Incident.crimes.through
    extra = 1


class CorrobAdminIn(admin.ModelAdmin):
    """
    inlines = [
        TimeInfoInlineIn, CommentsInlineIn, LocationInlineIn,
        ActorsRoleInlineIn, LabelInlineIn, CrimesInlineIn
    ]
    list_display = ('title_en',  'incident_details_en', )
    exclude = ('times', 'locations', 'actors_role', 'incident_comments', 'labels', 'crimes')
    """

class LocationInline(admin.TabularInline):
    model = Bulletin.locations.through
    extra = 1


class TimeInfoInline(admin.StackedInline):
    model = Bulletin.times.through
    extra = 1


class SourceInline(admin.TabularInline):
    model = Bulletin.sources.through
    extra = 1


class ActorsRoleInline(admin.TabularInline):
    model = Bulletin.actors_role.through
    extra = 1


class LabelInline(admin.TabularInline):
    model = Bulletin.labels.through


class CorrobAdmin(admin.ModelAdmin):
    """
    inlines = [
        TimeInfoInline, LocationInline, SourceInline,
        ActorsRoleInline, LabelInline,
    ]
    list_display = ('title_en', 'description_en', )
    exclude = ('times', 'locations', 'sources', 'actors_role', 'labels')
    """


class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_en', 'description_en', )
    readonly_fields = ('user', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


class TimeInfoAdmin(admin.ModelAdmin):
    list_display = ('time_from', 'time_to', 'comments_en', )


class ActorAdmin(reversion.VersionAdmin):
    pass


class ActorConditionAdmin(reversion.VersionAdmin):
    pass


class ActorRoleAdmin(reversion.VersionAdmin):
    pass


class RelationTypeAdmin(reversion.VersionAdmin):
    pass


class RoleTypeAdmin(reversion.VersionAdmin):
    pass


class EventTypeAdmin(reversion.VersionAdmin):
    pass


class StatusUpdateAdmin(reversion.VersionAdmin):
    pass


class LocationAdmin(reversion.VersionAdmin):
    pass


class SourceAdmin(reversion.VersionAdmin):
    pass


class SourceTypeAdmin(reversion.VersionAdmin):
    pass


class LabelAdmin(reversion.VersionAdmin):
    pass


class CrimeCategoryAdmin(reversion.VersionAdmin):
    pass


class MediaAdmin(reversion.VersionAdmin):
    pass


class CommentAdmin(reversion.VersionAdmin):
    pass


class PredefinedSearchAdmin(reversion.VersionAdmin):
    pass


class CorrobAdminRev(reversion.VersionAdmin, CorrobAdmin):
    pass


class CorrobAdminInRev(reversion.VersionAdmin, CorrobAdminIn):
    pass


class TimeInfoAdminRev(reversion.VersionAdmin, TimeInfoAdmin):
    pass
#class test(LockableAdmin, CorrobAdminInRev):
    #list_display = ('get_lock_for_admin',)

admin.site.register(Actor, ActorAdmin)
admin.site.register(ActorCondition, ActorConditionAdmin)
admin.site.register(ActorRole, ActorRoleAdmin)
admin.site.register(RelationType, RelationTypeAdmin)
admin.site.register(RoleType, RoleTypeAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Bulletin, CorrobAdminRev)
admin.site.register(StatusUpdate, StatusUpdateAdmin)
admin.site.register(TimeInfo, TimeInfoAdminRev)
admin.site.register(Location, LocationAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(SourceType, SourceTypeAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(CrimeCategory, CrimeCategoryAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PredefinedSearch, PredefinedSearchAdmin)
admin.site.register(Incident, CorrobAdminInRev)
#admin.site.register(Incident, test)
