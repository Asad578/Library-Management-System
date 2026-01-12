(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('alert-container');
    if (!container) return;

    const alerts = container.querySelectorAll('.alert');
    if (!alerts.length) return;

    function cleanupContainer() {
      if (!container.querySelector('.alert.show')) {
        container.remove();
      }
    }

    // Auto close after 3 seconds
    setTimeout(function () {
      alerts.forEach(function (el) {
        try {
          const bsAlert = bootstrap.Alert.getOrCreateInstance(el);
          el.addEventListener('closed.bs.alert', cleanupContainer);
          bsAlert.close();
        } catch (e) {
          el.remove();
          cleanupContainer();
        }
      });
    }, 3000);

    // Manual close
    alerts.forEach(function (el) {
      el.addEventListener('closed.bs.alert', cleanupContainer);
    });
  });
})();
