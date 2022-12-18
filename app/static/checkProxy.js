// checkProxy

// Check if the user is connected to the proxy server
var proxyServer = "http://192.168.178.56:8080";

// Make a GET request to the server-side script that checks the user's connection
var xhr = new XMLHttpRequest();
var url = "http://192.168.178.56:5000/index.html";
xhr.open("GET", url);
xhr.send();

// Wait for the response
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4 && xhr.status === 200) {
    // If the response is successful, check the response text
    var response = xhr.responseText;
    if (response === "connected") {
      // If the response text indicates that the user is connected to the proxy server, do nothing
    } else {
      // If the response text indicates that the user is not connected to the proxy server, display a pop-up message and redirect the user
      window.alert("You must be connected to the proxy server to access this website.");
      window.location.replace("http://192.168.178.56:5000/unauthorized");
    }
  }
}
 