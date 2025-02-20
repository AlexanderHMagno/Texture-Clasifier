import gradio as gr


article = """
    <div style='text-align: left; padding: 20px;'>
        <h2 style='margin-bottom: 1rem; color: #333; font-weight: 700;'>How to Use</h2>
        <ul style='padding-left: 20px; font-size: 1rem; color: #555;'>
            <li>Upload or drag-and-drop an image of a material texture</li>
            <li>The model will analyze the texture patterns</li>
            <li>View the predicted material category</li>
        </ul>
    </div>
    """

theme = gr.themes.Base().set(
        block_border_width="0px",
        block_radius="12px",  # Rounded corners for sections
        block_shadow="0 4px 8px rgba(0,0,0,0.2)",  # Soft shadow effect
        button_primary_background_fill="#007bff",  # Professional blue button
        button_primary_background_fill_hover="#0056b3",
        button_primary_text_color="#ffffff",
        button_secondary_background_fill="rgba(0,0,0,0.05)",
        button_secondary_background_fill_hover="rgba(0,0,0,0.1)",
        button_secondary_text_color="#333",
        input_background_fill="rgba(255, 255, 255, 0.8)",
        input_border_color="#d1d1d1",
        input_border_width="1px",
        input_shadow="0 2px 4px rgba(0,0,0,0.1)",
        input_radius="6px",
    )

css = """
        :root .dark {
            --body-background-fill: linear-gradient(45deg, rgba(2,0,36,1) 0%, rgba(69,9,121,1) 35%, rgba(89,9,121,1) 100%);
            --block-background-fill: rgba(2, 0, 36, 1)!important;
        }

        
        :root {
            --body-background-fill: linear-gradient(45deg, rgba(89,9,121,1) 0%, rgba(255,255,255,1) 90%);
            --block-background-fill: rgba(255, 255, 255, 1)!important;
        }

        .gradio-container {
            max-width: 900px;
            margin: auto;
            padding: 30px;
            background: transparent;
            border-radius: 12px;
            
        }

        .image-container {
            background: rgba(0,0,0,0.85);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            height: 250px;
        }

        .image-container img {
            max-width: 100%;
            border-radius: 10px;
            object-fit: cover;
        }


        button {
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
        }

        .gradio-button.primary {
            background: linear-gradient(45deg, #007bff, #0056b3);
            border: none;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
        }



        label {
            font-size: 0.5rem;
            font-weight: bold;
            color: #222;
            background: black;
            color: white;
            border: none;
        }
        .source-selection {
            display: none;
        }

        .unpadded_box, .output-class  {
          height: 96px !important;
        }

    """


check_categories = ["stone", "wood", "brick"]