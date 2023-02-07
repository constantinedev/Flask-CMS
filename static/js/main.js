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
      plugins:
        "export advlist autolink link linkchecker image imagetools importcss lists charmap print preview hr anchor pagebreak spellchecker searchreplace wordcount visualblocks visualchars advcode code fullscreen insertdatetime media mediaembed nonbreaking advtable save table contextmenu directionality formatpainter pageembed template paste textcolor codesample quickbars powerpaste casechange textpattern",
    },
    imagetools_toolbar:
      "rotateleft rotateright | flipv fliph | editimage imageoptions",
    toolbar:
      "print insertfile undo redo | styleselect | bold italic | code alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | export preview media fullpage | forecolor backcolor emoticons | codesample",
    contextmenu:
      "print template undo redo powerpaste | table inserttable | lists link image cell row column deletetable",
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
	document.addEventListener("focusin", (e) => {
    if (
      e.target.closest(
        ".tox-tinymce-aux, .moxman-window, .tam-assetmanager-root"
      ) !== null
    ) {
      e.stopImmediatePropagation();
    }
	});
	
});