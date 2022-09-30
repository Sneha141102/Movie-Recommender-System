function onPageLoad(){
    console.log("document loaded");
    var url = "https://movierecommender.onrender.com/get_movie_names";
    // fetch(url,function(data,status){
    //     console.log("got response from get_movie_names request");
    //     if(data){
            
           
    //     }
    // });
    fetch(url).then((res)=>res.text()).then((res)=>{
        data = res
        var selected_movie = document.getElementById("selected_movie");
    console.log(data);
    var movies = data.split(',');
    movies.forEach(movie=>{
        movie = movie.trim()
        selected_movie.options[selected_movie.options.length] = new Option(movie, movie);
    })
    })
    
   
   
}

    window.onload = onPageLoad;
