# class TicketCreateListSearchApiView(
#     mixins.CreateModelMixin,
#     # mixins.UpdateModelMixin,
#     generics.ListAPIView
# ):
#     """
#     Create Tickets
#     """
#     lookup_field = 'id'
#     serializer_class = s.TicketSerializer
#
#     def get_queryset(self):
#         qs = am.Ticket.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(
#                 Q(customer__name__icontains=query) |
#                 Q(customer__email__icontains=query) |
#                 Q(flight__route__origin__name__icontains=query) |
#                 Q(flight__route__origin__city__icontains=query) |
#                 Q(flight__route__destination__name__icontains=query) |
#                 Q(flight__route__destination__city__icontains=query)
#             ).distinct()
#         return qs
#
#     def perform_create(self, serializer):
#         serializer.save(customer=self.request.user)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     # def put(self, request, *args, **kwargs):
#     #     return self.update(request, *args, **kwargs)
#     #
#     # def patch(self, request, *args, **kwargs):
#     #     return self.update(request, *args, **kwargs)
#
#
# class TicketRetrieveApiView(generics.RetrieveAPIView):
#     """Retrieve Ticket"""
#     lookup_field = 'pk'
#     serializer_class = s.TicketSerializer
#     permission_classes = [p.IsOwnerOrReadOnly]
#     queryset = am.Ticket.objects.all()
#
#
# class TicketUpdateApiView(generics.UpdateAPIView):
#     """Update Tickets"""
#     lookup_field = 'pk'
#     serializer_class = s.TicketSerializer
#     permission_classes = [p.IsOwnerOrReadOnly]
#     queryset = am.Ticket.objects.all()
#
#
# class TicketDestroyApiView(generics.DestroyAPIView):
#     """Destroy Tickets"""
#     lookup_field = 'pk'
#     serializer_class = s.TicketSerializer
#     permission_classes = [p.IsOwnerOrReadOnly]
#     queryset = am.Ticket.objects.all()
