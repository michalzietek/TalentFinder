$(function() {
  $(document).on('click', ".delete-player-btn", function() {
    player = $(this).data('id');
    if ($(this).attr('data-list-url')) {
      $('#modal-delete-player-warning-warning').data('list-url', $(this).attr('data-list-url'));
    }
    $('#modal-delete-player-warning').modal('show');
    $('#modal-delete-player-warning').find('button[id="delete-submit-btn"]').data('id', player);
  });
});

$('#modal-delete-player-warning').on('click', '#delete-submit-btn', function() {
  player = $(this).data('id');
  $.ajax({
    url: $(this).attr('data-url'),
    data: {
      'player': player
    },
    success: function() {
        location.reload();
    }
  });
});
