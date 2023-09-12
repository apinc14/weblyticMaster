

    // Function to handle dropdown item click
    function handleDropdownItemClick(itemClass) {
        // Send an AJAX request to fetch new data based on the selected item
        $.ajax({
            url: "your-server-endpoint.php", // Replace with your server-side script or API endpoint
            type: "POST", // Use GET or POST as appropriate
            data: { selectedItem: itemClass },
            success: function (response) {
                // Handle the response data (update page content or refresh the page)
                location.reload(); // Refresh the page
            },
            error: function () {
                // Handle errors, e.g., display an error message
                alert("Error fetching data from the server.");
            }
        });
    }

    // Attach click event handlers to dropdown items
    $(".dropdown-item").on("click", function () {
        var itemClass = $(this).attr("class").split(" ")[1]; // Extract the class name
        handleDropdownItemClick(itemClass);
    });
