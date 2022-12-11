# an image cdn for post images, user avatar images, background images.

## Hierarchy
```bash
    - cdn
	+- <UID>
	    * img.<Ext>
	    * bg.<Ext>
	    +- other
		<postId>.<ext>
		+- <postId> // If a post has multiple images embedded in.
```

## routes

- `/Zimg/get` get request with followin form queries. id (Required), type (POST, img, bg), postID (if type == POST.), key.

- `/Zimg/add` adds an image with these parameters, id (Required), type, postID, key.

- `/Zimg/update` updates a user entry, bg or img.

- `/Zimg/Del` deletes an image.

