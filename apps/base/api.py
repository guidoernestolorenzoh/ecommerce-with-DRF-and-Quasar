from rest_framework import generics, viewsets


class GeneralViewSet(viewsets.ModelViewSet):
    serializer_class = None

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()



# class GeneralList(generics.ListCreateAPIView):
#     serializer_class = None
#
#     def get_queryset(self):
#         model = self.get_serializer().Meta.model
#         return model.objects.filter(state=True)
#
#
# class GeneralDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = None
#
#     def get_queryset(self):
#         model = self.get_serializer().Meta.model
#         return model.objects.filter(state=True)


