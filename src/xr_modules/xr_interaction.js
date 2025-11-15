/**
 * L - XR Interaction System
 * Handles laser controls, grabbing, and spatial manipulation
 */

class XRInteraction {
  constructor() {
    this.active = false;
    this.controllers = {
      left: { connected: false, position: [0, 0, 0], rotation: [0, 0, 0] },
      right: { connected: false, position: [0, 0, 0], rotation: [0, 0, 0] }
    };
    this.interactables = new Map();
    this.grabbed = null;
  }
  
  initialize() {
    console.log('✋ XR Interaction System initializing...');
    this.active = true;
    console.log('✴︎ Interaction System ACTIVE');
    return { success: true, status: 'ACTIVE' };
  }
  
  registerInteractable(id, config) {
    this.interactables.set(id, {
      id: id,
      type: config.type || 'OBJECT',
      position: config.position || [0, 0, 0],
      grabbable: config.grabbable !== undefined ? config.grabbable : true,
      clickable: config.clickable !== undefined ? config.clickable : true,
      onGrab: config.onGrab,
      onClick: config.onClick
    });
    
    return {
      success: true,
      interactableId: id
    };
  }
  
  grab(hand, interactableId) {
    const interactable = this.interactables.get(interactableId);
    
    if (!interactable) {
      return { success: false, error: 'INTERACTABLE_NOT_FOUND' };
    }
    
    if (!interactable.grabbable) {
      return { success: false, error: 'NOT_GRABBABLE' };
    }
    
    this.grabbed = {
      hand: hand,
      interactableId: interactableId,
      startTime: Date.now()
    };
    
    if (typeof interactable.onGrab === 'function') {
      interactable.onGrab(hand);
    }
    
    return {
      success: true,
      grabbed: interactableId,
      hand: hand
    };
  }
  
  release() {
    if (!this.grabbed) {
      return { success: false, error: 'NOTHING_GRABBED' };
    }
    
    const released = { ...this.grabbed };
    this.grabbed = null;
    
    return {
      success: true,
      released: released.interactableId,
      duration: Date.now() - released.startTime
    };
  }
  
  click(interactableId) {
    const interactable = this.interactables.get(interactableId);
    
    if (!interactable) {
      return { success: false, error: 'INTERACTABLE_NOT_FOUND' };
    }
    
    if (!interactable.clickable) {
      return { success: false, error: 'NOT_CLICKABLE' };
    }
    
    if (typeof interactable.onClick === 'function') {
      interactable.onClick();
    }
    
    return {
      success: true,
      clicked: interactableId,
      timestamp: Date.now()
    };
  }
  
  teleport(position) {
    return {
      success: true,
      action: 'TELEPORT',
      position: position,
      timestamp: Date.now()
    };
  }
  
  updateController(hand, position, rotation) {
    if (hand !== 'left' && hand !== 'right') {
      return { success: false, error: 'INVALID_HAND' };
    }
    
    this.controllers[hand] = {
      connected: true,
      position: position,
      rotation: rotation
    };
    
    return {
      success: true,
      hand: hand,
      controller: this.controllers[hand]
    };
  }
  
  getState() {
    return {
      success: true,
      active: this.active,
      controllers: { ...this.controllers },
      grabbed: this.grabbed,
      interactablesCount: this.interactables.size
    };
  }
}

module.exports = XRInteraction;
