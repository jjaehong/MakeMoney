from rest_framework import serializers
from .models import Article, Comment
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title','user')

    # override
    article = ArticleSerializer(read_only=True)
    user = UserSerializer(source='article.user', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):
    
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user','like_users')


class ArticleSerializer(serializers.ModelSerializer):

    user_set = UserSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


# class LikeSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model= Article
