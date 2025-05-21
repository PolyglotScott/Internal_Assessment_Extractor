#target photoshop

(function () {
    var inputFolder = Folder.selectDialog("Select the folder with HEIC images");
    if (!inputFolder) {
        alert("No folder selected. Exiting.");
        return;
    }

    var outputFolder = inputFolder; // Save PNGs in the same folder
    var files = inputFolder.getFiles(/\.(heic|HEIC)$/i);

    if (files.length === 0) {
        alert("No HEIC files found in the selected folder.");
        return;
    }

    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        if (file instanceof File) {
            open(file);
            var doc = app.activeDocument;

            var pngOptions = new PNGSaveOptions();
            pngOptions.interlaced = false;

            var saveFile = new File(outputFolder + "/" + doc.name.replace(/\.[^\.]+$/, ".png"));
            doc.saveAs(saveFile, pngOptions, true, Extension.LOWERCASE);

            doc.close(SaveOptions.DONOTSAVECHANGES);
        }
    }

    alert("Conversion completed!");
})();
