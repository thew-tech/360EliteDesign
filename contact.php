<?php
header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get POST data
    $data = json_decode(file_get_contents("php://input"), true);
    
    $name = isset($data['name']) ? htmlspecialchars($data['name']) : '';
    $email = isset($data['email']) ? htmlspecialchars($data['email']) : '';
    $service = isset($data['service']) ? htmlspecialchars($data['service']) : '';
    $message = isset($data['message']) ? htmlspecialchars($data['message']) : '';

    if (empty($name) || empty($email) || empty($message)) {
        echo json_encode(["status" => "error", "message" => "All required fields must be filled out."]);
        exit;
    }

    $to = "work@360elitedesign.com";
    $subject = "New Contact from $name";
    
    $body = "Name: $name\n";
    $body .= "Email: $email\n";
    $body .= "Interested Service: $service\n\n";
    $body .= "Project Details:\n$message\n";

    // Set headers
    $headers = "From: no-reply@360elitedesign.com\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();

    if (mail($to, $subject, $body, $headers)) {
        echo json_encode(["status" => "success", "message" => "Email sent successfully!"]);
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to send email via server."]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Invalid request method."]);
}
?>
