/* 
API Gateway
*/
api_gateway_name              = "tetris_api_dev"
api_gateway_stage_name        = "tetris_api_stage_dev"
api_gateway_access_log_format = "$context.identity.sourceIp $context.identity.caller $context.identity.user [$context.requestTime] \"$context.httpMethod $context.resourcePath $context.protocol\" $context.status $context.responseLength $context.requestId"
api_gateway_allow_origins     = ["https://d25ybu1lvw4x5b.cloudfront.net"]

/* 
Lambda
*/
send_message_to_sqs_function_name     = "lambda_send_message_to_sqs_function"
send_message_to_sqs_handler           = "register_evaluation_request.lambda_handler"
entry_to_competition_function_name    = "entry_to_competition_function_name"
entry_to_competition_handler          = "entry_competition_request.lambda_handler"
function_src_dir                      = "../scripts/api_to_sqs_lambda/src"
function_zip_output_path              = "archive/api_to_sqs_lambda_function.zip"
layer_src_dir                         = "../scripts/api_to_sqs_lambda/layer/packages"
layer_zip_output_path                 = "archive/layer.zip"
lambda_policy_send_message_to_sqs     = "SendMessageToSQSPolicy"
lambda_role_send_message_to_sqs       = "SendMessageToSQSLambdaRole"
lambda_send_message_to_sqs_layer_name = "lambda_send_message_to_sqs_layer_dev"

get_result_from_dynamodb_function_name              = "lambda_get_results_from_dynamodb_function"
get_result_from_dynamodb_function_handler           = "get_result_from_dynamodb.lambda_handler"
get_competition_entries_from_dynamodb_function_name = "lambda_get_competition_entries_from_dynamodb_function"
get_competition_entries_from_dynamodb_handler       = "get_entries_from_dynamodb.lambda_handler"
get_result_from_dynamodb_function_src_dir           = "../scripts/api_to_dynamodb_lambda/src"
get_result_from_dynamodb_function_zip_output_path   = "archive/get_result_from_dynamodb_lambda_function.zip"
get_result_from_dynamodb_layer_name                 = "lambda_get_result_from_dynamodb_layer_dev"
get_result_from_dynamodb_layer_src_dir              = "../scripts/api_to_dynamodb_lambda/layer/packages"
get_result_from_dynamodb_layer_zip_output_path      = "archive/get_result_from_dynamodb_layer.zip"
lambda_policy_get_result_from_dynamodb              = "GetResultsFromDynamoDBPolicy"
lambda_role_get_result_from_dynamodb                = "GetResultsFromDynamoDBLambdaRole"

/* 
CloudWatch
*/
cloudwatch_role_api_gateway_putlog    = "cloudwatch_role_api_gateway_putlog"
cloudwatch_api_gateway_log_group_name = "tetris_apigateway_accesslog"
cloudwatch_ecs_log_group_name         = "score_evaluation_ecs_log"
cloudwatch_ecs_scaleout_alarm         = "sqs_waiting_message_alarm"
cloudwatch_ecs_scalein_alarm          = "sqs_no_being processed_message_alarm"

/* 
SQS
*/
sqs_score_evaluation_name            = "score-evaluation-queue-dev"
sqs_score_evaluation_deadletter_name = "score-evaluation-deadletter-queue-dev"

/* 
ECS
*/
ecs_cluster_score_evaluation_name = "score_evaluation_cluster_dev"
ecs_task_definition_family        = "score_evaluation_family"
ecs_task_definition_image         = "public.ecr.aws/r2u8u6o1/tetris_score_evaluation:latest"
ecs_task_execution_role_name      = "ecsTaskExecutionRole"
ecs_task_role_name                = "scoreEvaluationTaskRole"
ecs_task_role_policy_name         = "scoreEvaluationTaskRolePolicy"
ecs_service_name                  = "score_evaluation_service_dev"

/* 
VPC
*/
vpc_cidr                 = "10.0.0.0/21"
vpc_tag                  = "tetris_score_server_dev"
subnet_cidr              = "10.0.0.0/24"
subnet_availability_zone = "ap-northeast-1c"

/* 
dynamodb
*/
dynamodb_table_name             = "tetris_score_table_dev"
dynamodb_competition_table_name = "tetris_competition_entry_table_dev"
