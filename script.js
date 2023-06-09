const Single=(method)=>{
    console.log(method);
}
// document.getElementById("retrive-form").addEventListener("submit", (e) => {
//     e.preventDefault();
//     const formData = new FormData(e.target);
//     console.log(formData.get("id"));
//     fetch(`http://127.0.0.1:8000/api/v3/app/events/${formData.get("id")}`).then((res) => res.json()).then((data) => {
//         document.getElementsByTagName("code")[0].innerHTML = JSON.stringify(data, null, 4);
//         hljs.highlightAll();
//         console.log(data)
//     });
// })