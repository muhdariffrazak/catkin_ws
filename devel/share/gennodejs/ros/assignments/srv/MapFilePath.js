// Auto-generated. Do not edit!

// (in-package assignments.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class MapFilePathRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.map_file_path = null;
    }
    else {
      if (initObj.hasOwnProperty('map_file_path')) {
        this.map_file_path = initObj.map_file_path
      }
      else {
        this.map_file_path = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MapFilePathRequest
    // Serialize message field [map_file_path]
    bufferOffset = _serializer.string(obj.map_file_path, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MapFilePathRequest
    let len;
    let data = new MapFilePathRequest(null);
    // Deserialize message field [map_file_path]
    data.map_file_path = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.map_file_path);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'assignments/MapFilePathRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2bfcad2d18ad637a0c527a2793461f29';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string map_file_path
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MapFilePathRequest(null);
    if (msg.map_file_path !== undefined) {
      resolved.map_file_path = msg.map_file_path;
    }
    else {
      resolved.map_file_path = ''
    }

    return resolved;
    }
};

class MapFilePathResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MapFilePathResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MapFilePathResponse
    let len;
    let data = new MapFilePathResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'assignments/MapFilePathResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MapFilePathResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: MapFilePathRequest,
  Response: MapFilePathResponse,
  md5sum() { return 'fad351900b5fbe0dbdabf42eace39648'; },
  datatype() { return 'assignments/MapFilePath'; }
};
