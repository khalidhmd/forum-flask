class BaseStore():
    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_instances = self.get_all()
        result = None
        for instance in all_instances:
            if instance.id == id:
                result = instance
                break
        return result

    def entity_exists(self, instance):
        return self.get_by_id(instance.id) is not None

    def delete(self, id):
        instance = self.get_by_id(id)
        self._data_provider.remove(instance)

    def update(self, instance):
        all_instances = self.get_all()
        for index, instance_in_list in enumerate(all_instances):
            if instance_in_list.id == instance.id:
                all_instances[index] = instance
                break


class MemberStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MemberStore.members, MemberStore.last_id)

    def get_by_name(self, member_name):
       return (member for member in self.get_all() if member.name == member_name)
    
    def get_members_with_posts(self, post_store):
        all_members = self.get_all()
        for member in all_members:
            posts = post_store.get_by_member_id(member.id)
            member.member_posts = posts
        return all_members

    def get_top(self, post_store, top_number):
        all_members = self.get_members_with_posts(post_store)
        all_members = sorted(all_members, key=lambda member: len(member.member_posts), reverse=True)
        return all_members[:top_number]



class PostStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(PostStore.posts, PostStore.last_id)

    def get_posts_by_date(self):
        all_posts = self.get_all()
        sorted(all_posts, key=lambda post: post.post_date, reverse=True)
        return all_posts

    def get_by_member_id(self, member_id):
        posts = []
        all_posts = self.get_all()
        for post in all_posts:
            if post.member_id == member_id:
                posts.append(post)
        return posts
