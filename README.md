# ZIMG CDN

## TODO

```bash
	
	$ [*] TODO GetUserAvatar(uuid: int) -> imgBytes       
	$ [*] TODO GetUserBackground(uuid: int) -> imgBytes
	$ [] TODO GetUserPostImgs(uuid: int, postId: int) -> imgBytes[]         
	$ [*] TODO PostUserAvatar(Mime: img, uuid: int) -> result          
	$ [*] TODO PostUserBackground(Mime: img, uuid: int) -> result
	$ [] TODO UpdateUserAvatar(uuid: int, NewMime: img) -> imgBytes         
	$ [] TODO UpdateUserBackground(uuid: int, NewMime: img) -> imgBytes             
	$ [] TODO PostUserPostImgs(Mimes: img[] | img, uuid, postId: int) -> result
	$ [] TOTAL TODOS: 8 (4/8). 

```
## Tested

```bash
	
	$ [*] TODO GetUserAvatar(uuid: int) -> imgBytes           
	$ [*] TODO GetUserBackground(uuid: int) -> imgBytes          
	$ [] TODO GetUserPostImgs(uuid: int, postId: int) -> imgBytes[]         
	$ [] TODO PostUserAvatar(Mime: img, uuid: int) -> result          
	$ [] TODO PostUserBackground(Mime: img, uuid: int) -> result
	$ [] TODO UpdateUserAvatar(uuid: int, NewMime: img) -> imgBytes         
	$ [] TODO UpdateUserBackground(uuid: int, NewMime: img) -> imgBytes             
	$ [] TODO PostUserPostImgs(Mimes: img[] | img, uuid, postId: int) -> result
	$ [] TOTAL TODOS: 8 (2/8). 

```

## Hierarchy

```bash
    - cdn
	+- <uuid>
	    * img.<Ext>
	    * bg.<Ext>
	    * Config.json
	    	# {"img": "img.jpeg", "bg": "bg.png"} config example
	    +- posts
			+-<postId> if it is more than one image, else: <postId>.<ext>
				* Config.json
					# {"img": [img1.jpeg, img2.png, img3.gif...]} example.
			* Config.json # {"img": [img1.jpeg, img2.png, img3.gif...]} example.
```

## routes

NOTE: Will be added when done with the todos above.

- `/Zimg/addAvatar` add avatar img expects `{"id": some id, "mime": imgMimeObject}`
- `/Zimg/<uuid>` get avatar img expected uuid.
- `/Zimg/addbg` add background expects `{"id": some id, "mime": imgMimeObject}`
- `/Zimg/bg/<uuid>`	get background expects uuid.


