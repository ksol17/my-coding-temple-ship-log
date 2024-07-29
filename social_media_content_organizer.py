def add_platform(content_dict, platform):
    if platform not in content_dict:
        content_dict[platform] = {}
        print(f"Platform '{platform}' added.")
    else:
        print(f"Platform '{platform}' already exists.")

def add_post_type(content_dict, platform, post_type):
    if platform in content_dict:
        if post_type not in content_dict[platform]:
            content_dict[platform][post_type] = []
            print(f"Post type '{post_type}' added to '{platform}'.")
        else:
            print(f"Post type '{post_type}' already exists in '{platform}'.")
    else:
        print(f"Platform '{platform}' does not exist.")

def add_post(content_dict, platform, post_type, post):
    if platform in content_dict and post_type in content_dict[platform]:
        content_dict[platform][post_type].append(post)
        print(f"Post added to '{platform}' under '{post_type}'.")
    else:
        print(f"Either platform '{platform}' or post type '{post_type}' does not exist.")

def display_content(content_dict):
    for platform, post_types in content_dict.items():
        print(f"Platform: {platform}")
        for post_type, posts in post_types.items():
            print(f" Post Type: {post_type}")
            for post in posts:
                print(f"     - {post}")


social_media_content = {
    "Facebook": {
        "Text": ["Hello World", "Python is fun!"],
        "Image": ["Beach photo", "Birthday party"]
    }
}

add_platform(social_media_content, "Instagram")
add_post_type(social_media_content, "Instagram", "Image")
add_post(social_media_content, "Instagram", "Image", "Sunset view")
display_content(social_media_content)