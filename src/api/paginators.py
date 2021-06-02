

class APIViewPaginationMixin():

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if not self.pagination_class:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator


    def paginate_queryset(self, queryset):
        
        if not self.paginator:
            return None

        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)


    def get_paginated_response(self, data):
        if not self.paginator:
            msg = "This view has no paginator attribute."
            raise AttributeError(msg)

        return self.paginator.get_paginated_response(data)