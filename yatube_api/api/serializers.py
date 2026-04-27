from rest_framework import serializers
from posts.models import Post, Comment, Group, Follow
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    group = serializers.SlugRelatedField(
        queryset=Group.objects.all(),
        slug_field='id',
        allow_null=True,
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')

    def validate_following(self, value):
        request = self.context.get('request')
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            if request.user == value:
                raise serializers.ValidationError(
                    'Нельзя подписаться на самого себя'
                )
            if Follow.objects.filter(
                user=request.user, following=value
            ).exists():
                raise serializers.ValidationError(
                    'Вы уже подписаны на этого пользователя'
                )
        return value
