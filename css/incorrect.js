const forms=document.getElementById("forms")
const fail=document.getElementById("message")
forms.addEventListener("submit",function(event){
    event.preventDefault();

    fail.style.display="block";
    
    setTimeout(() => {
      const formAction = forms.getAttribute('action'); // Get the URL from the action attribute
      const formData = new URLSearchParams(new FormData(form)).toString(); // Serialize form data
      window.location.href = `${formAction}?${formData}`; // Redirect with GET query parameters
      fail.style.display="none"
    }, 2000); // Adjust timing as needed
  });
