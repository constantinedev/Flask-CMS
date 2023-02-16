$(document).ready(function () {
	
	$("main").addClass("container-xxl");

	$("header").load('static/htm/header.html');
	$("footer").load("static/htm/footer.html");
	
	tinymce.init({
    selector: ".tinymce",
    width: "100%",
    min_height: 500,
    plugins: [
      "export advlist autolink link linkchecker image imagetools importcss lists charmap print preview hr anchor pagebreak spellchecker",
      "searchreplace wordcount visualblocks visualchars advcode code fullscreen insertdatetime media mediaembed nonbreaking advtable",
      "save table contextmenu directionality formatpainter pageembed template paste textcolor codesample quickbars powerpaste casechange textpattern",
    ],
    mobile: {
      plugins: "export advlist autolink link linkchecker image imagetools importcss lists charmap print preview hr anchor pagebreak spellchecker searchreplace wordcount visualblocks visualchars advcode code fullscreen insertdatetime media mediaembed nonbreaking advtable save table contextmenu directionality formatpainter pageembed template paste textcolor codesample quickbars powerpaste casechange textpattern",
    },
    imagetools_toolbar: "rotateleft rotateright | flipv fliph | editimage imageoptions",
    toolbar: "print insertfile undo redo | styleselect | bold italic | code alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | export preview media fullpage | forecolor backcolor emoticons | codesample",
    contextmenu: "print template undo redo powerpaste | table inserttable | lists link image cell row column deletetable",
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
	
<<<<<<< HEAD
  document.addEventListener("focusin", function (e) {
    if (e.target.closest(
      ".tox-tinymce-aux, .moxman-window, .tam-assetmanager-root"
    ) !== null) {
      e.stopImmediatePropagation();
    }
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
=======
  document.addEventListener("focusin", (e) => {
    if (
      e.target.closest(
        ".tox-tinymce-aux, .moxman-window, .tam-assetmanager-root"
      ) !== null
    ) {
      e.stopImmediatePropagation();
    }
  });
>>>>>>> b03eb0eaef9e9fce662613e724384e145dcf6fbd
	
});
