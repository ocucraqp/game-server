from rest_framework import serializers

from server.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'st_point',
            'status_hp',
            'status_arm',
            'status_luck',
        ]

    def validate(self, data):
        user = self.instance

        pre_st_point = user.st_point
        pre_st_hp = user.status_hp
        pre_st_arm = user.status_arm
        pre_st_luck = user.status_luck

        new_st_point = data.get('st_point')
        new_st_hp = data.get('status_hp')
        new_st_arm = data.get('status_arm')
        new_st_luck = data.get('status_luck')

        if pre_st_hp > new_st_hp or pre_st_arm > new_st_arm or pre_st_luck > new_st_luck:
            raise serializers.ValidationError('ステータスが下がっています')

        if new_st_point > pre_st_point:
            raise serializers.ValidationError('ステータスポイントが増えています')

        if pre_st_point + pre_st_hp + pre_st_arm + pre_st_luck != new_st_point + new_st_hp + new_st_arm + new_st_luck:
            raise serializers.ValidationError('ステータスポイントが正しく振り分けられていません')

        if new_st_point < 0:
            raise serializers.ValidationError('ステータスポイントが負になっています')

        return data
