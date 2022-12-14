from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = "__all__"
        # fields = ('title', 'content', 'cat')  # поля, к которым нужен доступ
