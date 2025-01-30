sta = 0
function see(){
	document.getElementById('intro').innerHTML = 'Learn and see amazing testimonies of some young men of the The Church Of Jesus Christ Of Latter Days Sanits and be strengten by the testimonies and sas you do so may you be bless. Amen';
	document.getElementById('now').innerHTML= 'See less';
console.log("wfuh")
function less(){
	document.getElementById('intro').innerHTML = 'Learn and see amazing testimonies of some young men of the The Church Of Jesus Christ Of Latter Days Sanits...;
	document.getElementById('now').innerHTML= 'Read more';
}

function(){
	if(sta == 0){
		see()
		sta = 1
	}else{
		less()
		sta = 0
	}
}