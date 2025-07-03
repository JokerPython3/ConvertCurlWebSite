function textCopy() {
    const textarea = document.getElementById("ksj");
    textarea.select(); 
    textarea.setSelectionRange(0, 99999); 
    document.execCommand("copy"); 
    alert("done copy");
}