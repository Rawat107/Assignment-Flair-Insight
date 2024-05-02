document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    
    var outputDiv = document.getElementById("output");
    outputDiv.innerHTML = "<h2>Submitted Data:</h2>";
    outputDiv.innerHTML += "<p><strong>Name:</strong> " + name + "</p>";
    outputDiv.innerHTML += "<p><strong>Email:</strong> " + email + "</p>";
});
