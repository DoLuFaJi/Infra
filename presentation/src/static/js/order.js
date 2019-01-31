// Chart.js scripts
// -- Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
// -- Bar Chart Example

Pusher.logToConsole = true;

// Configure Pusher instance
var pusher = new Pusher('4adcbc6f4cdd9aed0a57', {
  cluster: 'eu',
  encrypted: true
});
