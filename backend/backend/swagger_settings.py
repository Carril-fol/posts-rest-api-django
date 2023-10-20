from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Posts REST API',
        default_version='v1',
        description="""
        #### This REST API provides operations for managing posts, comments, and profiles (Posts).
        #### Through this API, users can create, read, update and delete Posts, comment on them and like them.

        ### Main Operations:

        #### Posts:

        * ##### Create a Post: Allows users to create a new post with title, description and tags.
        * ##### List Posts: Retrieves a list of available Posts.
        * ##### View a Post: Displays the details of a specific Post, including its title, description, and author.
        * ##### Update a Post: Allows users to modify their own existing post.
        * ##### Delete a Post: Allows users to delete their own post.
        * ##### Like a Post: Allows users to indicate if they like a Post.

        #### Comments:

        * ##### Add a Comment: Allows users to add comments to a Post.
        * ##### View Comments: Retrieves the comments associated with a specific Post.
        * ##### Like Comments: Allows users to like a comment.

        #### Profiles:
        
        * ##### Create a Profile: User profiles are created automatically when they register.
        * ##### Update a Profile: Allows users to update their profile
        * ##### Follow Profiles: Allows other users to follow Profiles of other users.

        #### Authentication:

        ##### The API requires authentication via a JWT token (JSON Web Token) to protect sensitive operations and ensure data security.

        ### Important Notes:

        * ##### This API is designed to be used by client applications and requires authentication with Token JWT.
        * ##### Posts can contain rich text (HTML) in their description.
        * ##### The API allows users to perform CRUD (Create, Read, Update and Delete) operations on their own Posts.
        * ##### Comments on Posts are an integral part of user interaction.

        """,
        terms_of_service='https://www.tu-terminos-de-servicio.com/', #Agregar
        contact=openapi.Contact(email='folco.carril@gmail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)