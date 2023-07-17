def create_youtube_video(title, description):
    return {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
     
def like(new_youtube_vid):
	if "likes" in new_youtube_vid:
		new_youtube_vid["likes"]+=1
	return new_youtube_vid

def like(new_youtube_vid):
	if "likes" in new_youtube_vid:
		new_youtube_vid["likes"]+=1
	return new_youtube_vid

def new_comment(new_youtube_vid,username,comment_text):
    new_youtube_video["comments"][username] = comment_text
    return video



