// Auto-generated. Do not edit!

// (in-package panthera_lights.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class LightStatus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Brake = null;
      this.HazardLight = null;
      this.SignalRight = null;
      this.SignalLeft = null;
      this.Autonomous = null;
      this.TeleOp = null;
      this.Beacon = null;
      this.Night = null;
      this.Day = null;
    }
    else {
      if (initObj.hasOwnProperty('Brake')) {
        this.Brake = initObj.Brake
      }
      else {
        this.Brake = 0;
      }
      if (initObj.hasOwnProperty('HazardLight')) {
        this.HazardLight = initObj.HazardLight
      }
      else {
        this.HazardLight = 0;
      }
      if (initObj.hasOwnProperty('SignalRight')) {
        this.SignalRight = initObj.SignalRight
      }
      else {
        this.SignalRight = 0;
      }
      if (initObj.hasOwnProperty('SignalLeft')) {
        this.SignalLeft = initObj.SignalLeft
      }
      else {
        this.SignalLeft = 0;
      }
      if (initObj.hasOwnProperty('Autonomous')) {
        this.Autonomous = initObj.Autonomous
      }
      else {
        this.Autonomous = 0;
      }
      if (initObj.hasOwnProperty('TeleOp')) {
        this.TeleOp = initObj.TeleOp
      }
      else {
        this.TeleOp = 0;
      }
      if (initObj.hasOwnProperty('Beacon')) {
        this.Beacon = initObj.Beacon
      }
      else {
        this.Beacon = 0;
      }
      if (initObj.hasOwnProperty('Night')) {
        this.Night = initObj.Night
      }
      else {
        this.Night = 0;
      }
      if (initObj.hasOwnProperty('Day')) {
        this.Day = initObj.Day
      }
      else {
        this.Day = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LightStatus
    // Serialize message field [Brake]
    bufferOffset = _serializer.uint8(obj.Brake, buffer, bufferOffset);
    // Serialize message field [HazardLight]
    bufferOffset = _serializer.uint8(obj.HazardLight, buffer, bufferOffset);
    // Serialize message field [SignalRight]
    bufferOffset = _serializer.uint8(obj.SignalRight, buffer, bufferOffset);
    // Serialize message field [SignalLeft]
    bufferOffset = _serializer.uint8(obj.SignalLeft, buffer, bufferOffset);
    // Serialize message field [Autonomous]
    bufferOffset = _serializer.uint8(obj.Autonomous, buffer, bufferOffset);
    // Serialize message field [TeleOp]
    bufferOffset = _serializer.uint8(obj.TeleOp, buffer, bufferOffset);
    // Serialize message field [Beacon]
    bufferOffset = _serializer.uint8(obj.Beacon, buffer, bufferOffset);
    // Serialize message field [Night]
    bufferOffset = _serializer.uint8(obj.Night, buffer, bufferOffset);
    // Serialize message field [Day]
    bufferOffset = _serializer.uint8(obj.Day, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LightStatus
    let len;
    let data = new LightStatus(null);
    // Deserialize message field [Brake]
    data.Brake = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [HazardLight]
    data.HazardLight = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [SignalRight]
    data.SignalRight = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [SignalLeft]
    data.SignalLeft = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [Autonomous]
    data.Autonomous = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [TeleOp]
    data.TeleOp = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [Beacon]
    data.Beacon = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [Night]
    data.Night = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [Day]
    data.Day = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'panthera_lights/LightStatus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e88e78a8e709ed3fa5e5e18d48c62d5d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 Brake
    uint8 HazardLight
    uint8 SignalRight
    uint8 SignalLeft
    uint8 Autonomous
    uint8 TeleOp
    uint8 Beacon
    uint8 Night
    uint8 Day
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LightStatus(null);
    if (msg.Brake !== undefined) {
      resolved.Brake = msg.Brake;
    }
    else {
      resolved.Brake = 0
    }

    if (msg.HazardLight !== undefined) {
      resolved.HazardLight = msg.HazardLight;
    }
    else {
      resolved.HazardLight = 0
    }

    if (msg.SignalRight !== undefined) {
      resolved.SignalRight = msg.SignalRight;
    }
    else {
      resolved.SignalRight = 0
    }

    if (msg.SignalLeft !== undefined) {
      resolved.SignalLeft = msg.SignalLeft;
    }
    else {
      resolved.SignalLeft = 0
    }

    if (msg.Autonomous !== undefined) {
      resolved.Autonomous = msg.Autonomous;
    }
    else {
      resolved.Autonomous = 0
    }

    if (msg.TeleOp !== undefined) {
      resolved.TeleOp = msg.TeleOp;
    }
    else {
      resolved.TeleOp = 0
    }

    if (msg.Beacon !== undefined) {
      resolved.Beacon = msg.Beacon;
    }
    else {
      resolved.Beacon = 0
    }

    if (msg.Night !== undefined) {
      resolved.Night = msg.Night;
    }
    else {
      resolved.Night = 0
    }

    if (msg.Day !== undefined) {
      resolved.Day = msg.Day;
    }
    else {
      resolved.Day = 0
    }

    return resolved;
    }
};

module.exports = LightStatus;
