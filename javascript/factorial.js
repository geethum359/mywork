function fact()
{
    var a,fa;
    a=document.getElementById("n").value;
    fa=1;
    for(i=1;i<=a;i++)
    {
       fa=fa*i ;
    }
    document.getElementById("re").innerHTML ="factiorial of "+a+" is" + fa;
   
}
