from django.db import models

# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    pub_data = models.DateTimeField('date published')

    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname