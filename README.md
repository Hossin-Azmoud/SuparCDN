# an image cdn for post images, user avatar images, background images.

## TODO

```bash
	$ [] TODO GetUserAvatar(uuid: int) -> imgBytes           
	$ [] TODO GetUserBackground(uuid: int) -> imgBytes          
	$ [] TODO GetUserPostImgs(uuid: int, postId: int) -> imgBytes[]         
	$ [] TODO PostUserAvatar(Mime: img, uuid: int) -> result          
	$ [] TODO PostUserBackground(Mime: img, uuid: int) -> result
	$ [] TODO UpdateUserAvatar(uuid: int, NewMime: img) -> imgBytes         
	$ [] TODO UpdateUserBackground(uuid: int, NewMime: img) -> imgBytes             
	$ [] TODO PostUserPostImgs(Mimes: img[] | img, uuid, postId: int) -> result
	$ [] TOTAL TODOS: 8 (0/8). 
```

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
NOTE: Will be added when done with the todos above.

