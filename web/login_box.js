function login_result() 
{   
    var user_id = document.getElementById("user_id").value;
    var user_pw = document.getElementById("user_pw").value;

    display_values={0:"none", 1:"block"}
    var display_value = 0;

    if (user_id === "a" && user_pw === "1")
    {   
        document.getElementById("form").style.display="none";
        document.getElementById("login_s").style.display="block";
        document.getElementById("login_f").style.display="none";
    }
    else
    {
        document.getElementById("form").style.display="block";
        document.getElementById("login_s").style.display="none";
        document.getElementById("login_f").style.display="block";
    }
    return false;
}