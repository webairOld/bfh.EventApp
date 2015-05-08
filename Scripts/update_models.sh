#!/bin/sh
MODEL_PATH="./EventApp/Model.xcdatamodeld"
OUTPUT_PATH="./EventApp/Classes/Core/Models"
./Scripts/mogenerator \
	--v2 \
	--swift \
	--base-class-import "THCCoreData" \
	--protocol "NamedManagedObject" \
	-m "${MODEL_PATH}/${LATEST_VERSION}" \
	-H "${OUTPUT_PATH}" \
	-M "${OUTPUT_PATH}/Generated" 

