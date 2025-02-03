const form=document.getElementById("teacher")
const success=document.getElementById("message")
form.addEventListener("submit",function(event){
    event.preventDefault();

    success.style.display="block";
    
    setTimeout(() => {
      const formAction = form.getAttribute('action'); // Get the URL from the action attribute
      const formData = new URLSearchParams(new FormData(form)).toString(); // Serialize form data
      window.location.href = `${formAction}?${formData}`; // Redirect with GET query parameters
      success.style.display="none"
    }, 2000); // Adjust timing as needed
  });
