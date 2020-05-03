from django.contrib import admin

from server.battles.models import EnemyType, Enemy, Contribution

admin.register(EnemyType, Enemy,Contribution)
