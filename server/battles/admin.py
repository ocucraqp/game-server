from django.contrib import admin

from server.battles.models import EnemyType, Enemy, Contribution

admin.site.register(EnemyType)
admin.site.register(Enemy)
admin.site.register(Contribution)
