document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.custom-fade-alert');
        setTimeout(function () {
        alerts.forEach(function (alert) {
            // Trigger reflow to make sure transition works reliably
            alert.offsetHeight; // force layout reflow

            alert.classList.add('fade-out');

            // Wait until opacity transition ends before removing
            alert.addEventListener('transitionend', function () {
                alert.remove();
            });
        });
    }, 1000); // Adjust delay as needed
});