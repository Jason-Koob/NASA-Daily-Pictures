const nasaPics = async () => {
    let response = await fetch(`https://api.nasa.gov/planetary/apod?api_key=4srFhHOenX9iR2vh7Am9mLrR9DXdKWOA9R7Yf6IS`);
    let json = await response.json()
    let summary = `${json.hdurl}`

    console.log(summary)
    return summary
    
};

const content = `${nasaPics}}`

const maincontent = document.querySelector(".maincontent")

const pic = document.createElement("img")
pic.classList.add("PICTURE")
pic.setAttribute("PICTURE", "PICTURE_VALUE")

maincontent.append(nasaPics())

maincontent.innerHTML += `src="${content}"`