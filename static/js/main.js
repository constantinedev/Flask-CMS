$(document).ready(function () {
	
	$("main").addClass("container-xxl");

	$("header").load('static/htm/header.html');
	$("footer").load("static/htm/footer.html");
	
  // Check if geolocation is supported by the browser
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
	} else {
		alert("Geolocation is not supported by this browser.");
	}

	// Function to show the user's position
	function showPosition(position) {
		var latitude = position.coords.latitude;
		var longitude = position.coords.longitude;
		// $('[name="lat"]').val(latitude);
		// $('[name="lon"]').val(longitude);
	};

  ///click FUNCTION
  let now = new Date();
	let tZ = Intl.DateTimeFormat().resolvedOptions().timeZone;
	
	function javaClock(callback) {
		setInterval(function () {
			var clock_now = new Date();
			callback(clock_now);
		}, 1000);
	};

	javaClock(function (time) {
		var options = {
			day: "2-digit",
			month: "2-digit",
			year: "numeric",
			hour: "2-digit",
			hour12: true,
			timeZoneName: "short",
			minute: "numeric",
			second: "numeric",
		};
    $("#live_clock").text("(" + tZ + ") " + time.toLocaleString("en-US", options));
  });

  ///TIME Function convert datetime to ISOString
  // let now_clin = new Date();
	// var isoDT = now_clin.toISOString();
	var timezoneOffset = now.getTimezoneOffset() * 60000;
	var localISOTime = new Date(now - timezoneOffset).toISOString().slice(0, -1);
		
	/// Gettings Timezone Offset +00:00
	var timezoneOffset = now.getTimezoneOffset();
	var sign = timezoneOffset > 0 ? "-" : "+";
	var hours = Math.abs(Math.floor(timezoneOffset / 60)).toString().padStart(2, "0");
	var minutes = Math.abs(timezoneOffset % 60).toString().padStart(2, "0");
	var timezoneOffsetString = sign + hours + ":" + minutes;

  let isoretudt = localISOTime + timezoneOffsetString;

  //Ad-Blocker Detect
	(function(){
		var test = document.createElement('div');
		test.innerHTML = '&nbsp;';
		test.className = 'adsbox';
		document.body.appendChild(test);
		window.setTimeout(function() {
			if (test.offsetHeight === 0) {
				alert("Please stop Ad-Blocker Extension to continue brwosing!");
			} else {				
				//alert("not active");
			}
			test.remove();
		}, 100);
  })();
  
  // Make an HTTP GET request using $.ajax()
	$.ajax({
		url: "https://api64.ipify.org?format=json",
		method: "GET",
		dataType: "json",
		success: function (data) {
			// Extract the IP address from the response
      ip_add = data.ip;  
      // console.log(ip_add);
			// Display the IP address in an element with the ID "ip_addr"
			// $("#ip_addr").text(ip_addr);
		},
		error: function () {
			// Handle any errors that occur during the API request
      $(".hidden-info").css({"display": "block"});
			$("#ip_addr").text("Turn off your ad-block extension and reload again.");
		}
  });

	tinymce.init({
    selector: ".tinymce",
    width: "100%",
    min_height: 500,
    plugins: [
      "export advlist autolink link linkchecker image imagetools importcss lists charmap print preview hr anchor pagebreak spellchecker styleselect",
      "searchreplace wordcount visualblocks visualchars advcode code fullscreen insertdatetime media mediaembed nonbreaking advtable fontsize",
      "save table contextmenu directionality formatpainter pageembed template paste textcolor codesample quickbars powerpaste casechange textpattern",
    ],
    mobile: {
      plugins: "export advlist autolink link linkchecker image imagetools importcss styleselect lists charmap print fontsize preview hr anchor pagebreak spellchecker searchreplace wordcount visualblocks visualchars advcode code fullscreen insertdatetime media mediaembed nonbreaking advtable save table contextmenu directionality formatpainter pageembed template paste textcolor codesample quickbars powerpaste casechange textpattern",
    },
    imagetools_toolbar: "rotateleft rotateright | flipv fliph | editimage imageoptions",
    toolbar: "print insertfile undo redo | formatselect fontselect fontsizeselect | bold italic | code alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | export preview media fullpage | forecolor backcolor emoticons | codesample",
    contextmenu: "print template undo redo powerpaste formatselect fontselect fontsizeselect | code alignleft aligncenter alignright alignjustify | table inserttable | lists link image cell row column deletetable",
    fontsize_formats: "6pt 7pt 8pt 9pt 10pt 11pt 12pt 14pt 16pt 18pt 20pt 22pt 24pt",
    save_enablewhendirty: true,
    file_picker_types: "file image media",
    images_upload_url: "/panel?mod=imgupload",
    images_file_types: "jpg,svg,png,jpge,webp",
    paste_data_images: true,
    automatic_uploads: true,
    images_reuse_filename: false,
    images_upload_base_path: "/static/uploads",
    codesample_languages: [
      { text: "HTML/XML", value: "markup" },
      { text: "JavaScript", value: "javascript" },
      { text: "CSS", value: "css" },
      { text: "Processing", value: "processing" },
      { text: "Python", value: "python" },
    ],
  });
	
  // Example starter JavaScript for disabling form submissions if there are invalid fields
	(function () {
		'use strict';
		window.addEventListener('load', function () {
			// Fetch all the forms we want to apply custom Bootstrap validation styles to
			var forms = document.getElementsByClassName('needs-validation');
			// Loop over them and prevent submission
			var validation = Array.prototype.filter.call(forms, function (form) {
				form.addEventListener('submit', function (event) {
					if (form.checkValidity() === false) {
						event.preventDefault();
						event.stopPropagation();
					}
					form.classList.add('was-validated');
				}, false);
			});
		}, false);
  })();
  
  //TinyMCE for Model
	document.addEventListener('focusin', (e) => {
		if (e.target.closest(".tox-tinymce-aux, .moxman-window, .tam-assetmanager-root") !== null) {
			e.stopImmediatePropagation();
		}
	});

  var darkModeToggle = document.querySelector("#darkSwitch");
  darkModeToggle.addEventListener("change", (event) => {
    document.body.classList.toggle("dark-mode", event.target.checked);
  });
	
  var darkMode = localStorage.getItem("darkMode");
  if (darkMode === "enabled") {
    document.body.classList.add("dark-mode");
  }

  document.querySelector(".form-switch").addEventListener("click", function () {
    // Toggle the "dark-mode" class on the body
    document.body.classList.toggle("dark-mode");

    // Save the state of the switch to local storage
    if (document.body.classList.contains("dark-mode")) {
      localStorage.setItem("darkMode", "enabled");
    } else {
      localStorage.setItem("darkMode", "disabled");
    }
  });

});