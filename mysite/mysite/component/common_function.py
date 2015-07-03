class Queue(list):
    def push(self, item):
        self.append(item)
    def pull(self):
        try:
            ret =  self[0]
        except IndexError,e:
            raise IndexError("Queue is empty")

        del self[0]
        return ret

class Tools():
    def hasExistParams(self,request_obj, item, request_method = 'GET'):
        has_exist_params = True
        if request_method == 'GET':
            for i in item:
                has_exist_params = request_obj.GET.has_key(i)
        elif request_method == 'POST':
            for i in item:
                has_exist_params = request_obj.POST.has_key(i)
        return has_exist_params